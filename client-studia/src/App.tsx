import * as react from 'react';
import { Routes, Route, Outlet } from 'react-router-dom';
import { AuthLayout } from './layout/AuhtLayout';
import { Login } from './pages/auth/Login';
import { Register } from './pages/auth/Register';
import { NotFoundPage } from './pages/helper/404';
import { TeacherRegister } from './pages/auth/register-role/Teacher';
import { StudentRegister } from './pages/auth/register-role/Student';
import { AuthContext } from './context/react/authContext';
import { RoleRegister, UserRegister } from './types/auth/type';
import { Home } from './pages/Home';
import { AuthWrapper } from './service/AuthWrapper';

export const App: react.FC = () => {
  const [user, setUser] = react.useState<UserRegister>({
    username: '',
    email: '',
    name: '',
    role: RoleRegister.student,
    password: '',
  });

  const changeUser = (data: UserRegister) => {
    setUser({
      ...data,
    });
  };
  return (
    <>
      <Routes>
        <Route
          path='/'
          element={
            // <AuthWrapper>
            <Outlet />
            // </AuthWrapper>
          }>
          <Route path='' element={<Home />} />
        </Route>
        <Route path='/auth' element={<AuthLayout />}>
          <Route path='login' element={<Login />} />
          <Route
            path='register'
            element={
              <AuthContext.Provider value={{ user, changeUser }}>
                <Outlet />
              </AuthContext.Provider>
            }>
            <Route path='' element={<Register />} />
            <Route path='teacher' element={<TeacherRegister />} />
            <Route path='student' element={<StudentRegister />} />
          </Route>
        </Route>
        <Route path='*' element={<NotFoundPage />} />
      </Routes>
    </>
  );
};
