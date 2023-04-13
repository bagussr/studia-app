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
} from '@chakra-ui/react';
import { Link as LinkRouter } from 'react-router-dom';
import { useForm } from 'react-hook-form';

import logo from '../../assets/images/logo.png';

export const Login: react.FC = () => {
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
          as='form'
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
              Masuk
            </Heading>
            <Link as={LinkRouter} to='../register'>
              Daftar
            </Link>
          </Box>
          <FormControl isRequired>
            <Input placeholder='Nomor Ponsel atau Email' />
          </FormControl>
          <FormControl isRequired>
            <Input placeholder='Kata Sandi' type='password' />
          </FormControl>
          <Button colorScheme='gray'>Masuk</Button>
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
        </Container>
      </Box>
    </>
  );
};
