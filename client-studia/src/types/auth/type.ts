export enum RoleRegister {
  teacher = 'TEACHER',
  student = 'STUDENT',
}

export interface UserLogin {
  username: string;
  password: string;
}

export interface UserRegister {
  role?: RoleRegister;
  name: string;
  username: string;
  email: string;
  password: string;
}

export interface Token {
  accessToken: string;
  refreshToken: string;
}

export interface AuthToken {
  role: string;
  id: string;
  token: Token;
}

export interface RegisterInput extends UserRegister {
  confirmPassword: string;
  _password2?: string;
}

export type ChangeUser = (data: UserRegister) => void;

export type HandleLogin = (data: UserLogin) => void;

export type HandleRegister = (data: RegisterInput) => void;
