import * as react from 'react';
import { useNavigate } from 'react-router-dom';

import { useAppSelector, useAppDispatch } from '../context/redux/hooks';
import { authLogin } from '../context/redux/reducers/auth';
import { AuthToken } from '../types/auth/type';

interface Props {
  children: React.ReactElement;
}

export const AuthWrapper: react.FC<Props> = ({ children }) => {
  const auth = useAppSelector(state => state.auth);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();
  const [loading, setLoading] = react.useState<boolean>(false);
  react.useEffect(() => {
    const _auth: AuthToken = JSON.parse(window.localStorage.getItem('auth'));
    if (auth.id === null) {
      if (_auth === null) {
        setLoading(true);
        navigate('../auth/login');
      } else {
        setLoading(true);
        dispatch(authLogin(_auth));
        null;
      }
    } else {
      setLoading(true);
      navigate('../../../');
    }
  }, []);
  if (loading) {
    return <>{children}</>;
  }
};
