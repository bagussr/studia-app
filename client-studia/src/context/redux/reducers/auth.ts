import { CaseReducer, createSlice, PayloadAction } from '@reduxjs/toolkit';
import type { RootState } from '../store';
import { AuthToken } from '../../../types/auth/type';

const intialState: AuthToken = {
  role: null,
  id: null,
  token: {
    accessToken: '',
    refreshToken: '',
  },
};

const loginReducer: CaseReducer<AuthToken, PayloadAction<AuthToken>> = (
  state,
  action
) => {
  return {
    ...state,
    ...action,
  };
};

export const authSlice = createSlice({
  name: 'auth-slice',
  initialState: intialState,
  reducers: {
    authLogin: loginReducer,
  },
});

export const { authLogin } = authSlice.actions;

export const selectAuth = (state: RootState) => state.auth.id;

export default authSlice.reducer;
