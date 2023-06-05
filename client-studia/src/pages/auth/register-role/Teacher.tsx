import * as react from 'react';

import {
  Box,
  Image,
  Container,
  Input,
  FormControl,
  Link,
  Heading,
  Button,
  Text,
  Divider,
  Center,
  FormErrorMessage,
} from '@chakra-ui/react';
import { Link as LinkRouter } from 'react-router-dom';
import { useForm } from 'react-hook-form';

import logo from '../../../assets/images/logo.png';
import { AuthContext } from '../../../context/react/authContext';
import {
  ChangeUser,
  HandleRegister,
  RegisterInput,
  UserRegister,
} from '../../../types/auth/type';

export const TeacherRegister: react.FC = () => {
  const { user, changeUser }: { user: UserRegister; changeUser: ChangeUser } =
    react.useContext(AuthContext);
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors, isSubmitting },
  } = useForm<RegisterInput>();

  const handleRegister: HandleRegister = (data: RegisterInput) => {
    data._password2 = data.confirmPassword;
    delete data.confirmPassword;

    console.log({ ...user, ...data });
  };

  const handleCheckUsername = (event: react.ChangeEvent<HTMLInputElement>) => {
    console.log(event.target.value);
  };

  return (
    <>
      <Box
        display='flex'
        alignItems='center'
        w='full'
        flexDir='column'
        justifyContent={{ base: 'center', sm: 'start' }}
        mt={{ base: '0', sm: '32' }}>
        <Image src={logo} alt='logo studia' />
        <Container
          onSubmit={handleSubmit(handleRegister)}
          as='form'
          w={{ xl: '2/3', base: '3/4' }}
          display='flex'
          flexDir='column'
          rowGap={4}>
          <Box
            display='flex'
            justifyContent='space-between'
            alignItems='end'
            mb={{ sm: '2', base: '0' }}>
            <Heading as='h2' fontSize={{ base: 'xl', sm: '2xl' }}>
              Guru
            </Heading>
            <Link as={LinkRouter} to='../../login'>
              Masuk
            </Link>
          </Box>
          <FormControl>
            <Input
              placeholder='Nama'
              {...register('name', {
                required: 'Name is required',
              })}
            />
          </FormControl>
          <FormControl>
            <Input
              placeholder='Username'
              {...register('username', {
                required: 'Username is required',
                onBlur: handleCheckUsername,
              })}
            />
          </FormControl>
          <FormControl isInvalid={errors?.email ? true : false}>
            <Input
              placeholder='Email'
              type='email'
              {...register('email', {
                required: 'Email is required',
              })}
            />
            <FormErrorMessage>{errors?.email?.message}</FormErrorMessage>
          </FormControl>
          <FormControl isInvalid={errors?.password ? true : false}>
            <Input
              placeholder='Kata Sandi'
              type='password'
              {...register('password', {
                required: 'Password is required',
                minLength: {
                  value: 8,
                  message: 'Password must be at least 8 characters',
                },
              })}
            />
            <FormErrorMessage>{errors?.password?.message}</FormErrorMessage>
          </FormControl>
          <FormControl isInvalid={errors?.confirmPassword ? true : false}>
            <Input
              placeholder='Konfirmasi Kata Sandi'
              type='password'
              {...register('confirmPassword', {
                required: 'Confirm Password is required',
                validate: {
                  passwordValidaton: (val: string) => {
                    if (watch('password') !== val) {
                      return 'Your password not macth';
                    }
                  },
                },
              })}
            />
            <FormErrorMessage>
              {errors?.confirmPassword?.message}
            </FormErrorMessage>
          </FormControl>
          <Button colorScheme='gray' isLoading={isSubmitting} type='submit'>
            Daftar
          </Button>
        </Container>
      </Box>
    </>
  );
};
