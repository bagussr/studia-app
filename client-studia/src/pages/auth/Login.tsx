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
  FormErrorMessage,
  Center,
  Divider,
} from '@chakra-ui/react';
import { Link as LinkRouter } from 'react-router-dom';
import { useForm } from 'react-hook-form';

import logo from '../../assets/images/logo.png';
import google from '../../assets/images/google-logo.webp';
import type { HandleLogin, UserLogin } from '../../types/auth/type';

export const Login: react.FC = () => {
  const {
    handleSubmit,
    register,
    formState: { errors, isSubmitting },
  } = useForm<UserLogin>();

  const handleLogin: HandleLogin = (data: UserLogin) => {
    console.log(data);
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
          onSubmit={handleSubmit(handleLogin)}
          as='form'
          w={{ md: '2/3', base: '3/4' }}
          display='flex'
          flexDir='column'
          rowGap={4}>
          <Box
            display='flex'
            justifyContent='space-between'
            alignItems='end'
            mb={{ sm: '2', base: '0' }}>
            <Heading as='h2' fontSize={{ base: 'xl', sm: '2xl' }}>
              Masuk
            </Heading>
            <Link as={LinkRouter} to='../register'>
              Daftar
            </Link>
          </Box>
          <FormControl isInvalid={errors?.username ? true : false}>
            <Input
              placeholder='Username atau Email'
              {...register('username', {
                required: 'Username or Email is Required',
              })}
            />
            <FormErrorMessage>{errors?.username?.message}</FormErrorMessage>
          </FormControl>
          <FormControl isInvalid={errors?.password ? true : false}>
            <Input
              placeholder='Kata Sandi'
              type='password'
              {...register('password', {
                required: 'Password is Required',
                minLength: {
                  value: 8,
                  message: 'Password must be at least 8 characters ',
                },
              })}
            />
            <FormErrorMessage>{errors?.password?.message}</FormErrorMessage>
          </FormControl>
          <Button
            colorScheme='gray'
            isLoading={isSubmitting}
            type='submit'
            fontSize={{ base: 'sm', lg: 'md' }}>
            Masuk
          </Button>
          <Text alignSelf='start' mt='5'>
            Lupa kata sandi? <Link as={LinkRouter}>Klik disini!</Link>
          </Text>
          <Box position='relative' mt={5}>
            <Center>
              <Text
                position='absolute'
                color='gray.300'
                display='inline-block'
                bg='white'
                px='3'
                zIndex={100}>
                atau masuk dengan
              </Text>
              <Divider />
            </Center>
          </Box>
          <Button
            mt='5'
            display='flex'
            variant='google'
            fontSize={{ base: 'sm', lg: 'md' }}>
            <Image
              src={google}
              height={{ lg: '6', base: '4' }}
              mr={{ lg: '4', base: '2' }}
            />{' '}
            Masuk dengan Google
          </Button>
        </Container>
      </Box>
    </>
  );
};
