import * as react from 'react';
import { Box, Image, Container, Link, Heading, Button } from '@chakra-ui/react';
import { Link as LinkRouter, useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';

import logo from '../../assets/images/logo.png';

export const Register: react.FC = () => {
  const navigate = useNavigate();
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
          w={{ sm: '1/2', xl: '2/3', base: '3/4' }}
          display='flex'
          flexDir='column'
          rowGap={4}>
          <Box
            display='flex'
            justifyContent='space-between'
            alignItems='end'
            mb={{ sm: '2', base: '0' }}>
            <Heading as='h2' fontSize={{ base: 'xl', sm: '2xl' }}>
              Daftar
            </Heading>
            <Link as={LinkRouter} to='../login'>
              Masuk
            </Link>
          </Box>
          <Box display='flex' flexDir='column' rowGap={6}>
            <Button
              w='full'
              colorScheme='gray'
              py={6}
              borderRadius='xl'
              onClick={() => {
                navigate('teacher');
              }}>
              Guru
            </Button>
            <Button
              w='full'
              colorScheme='gray'
              py={6}
              borderRadius='xl'
              onClick={() => {
                navigate('student');
              }}>
              Murid
            </Button>
          </Box>
        </Container>
      </Box>
    </>
  );
};
