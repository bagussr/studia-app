import * as react from 'react';
import { Routes, Route, Outlet } from 'react-router-dom';
import { AuthLayout } from './layout/AuhtLayout';
import { Login } from './pages/auth/Login';
import { Register } from './pages/auth/Register';
import { NotFoundPage } from './pages/helper/404';
import { TeacherRegister } from './pages/auth/register-role/Teacher';
import { StudentRegister } from './pages/auth/register-role/Student';

export const App: react.FC = () => {
  return (
    <>
      <Routes>
        <Route
          path='/'
          element={
            <>
              <h1>Hello Wolrd</h1>
            </>
          }
        />
        <Route path='/auth' element={<AuthLayout />}>
          <Route path='login' element={<Login />} />
          <Route path='register'>
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
