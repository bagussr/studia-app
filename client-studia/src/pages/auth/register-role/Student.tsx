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

import logo from '../../../assets/images/logo.png';

export const StudentRegister: react.FC = () => {
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
              Murid
            </Heading>
            <Link as={LinkRouter} to='../../login'>
              Masuk
            </Link>
          </Box>
          <FormControl isRequired>
            <Input placeholder='Nama' />
          </FormControl>
          <FormControl isRequired>
            <Input placeholder='Nomor Ponsel atau Email' />
          </FormControl>
          <FormControl isRequired>
            <Input placeholder='Kata Sandi' type='password' />
          </FormControl>
          <FormControl isRequired>
            <Input placeholder='Konfirmasi Kata Sandi' type='password' />
          </FormControl>
          <Button colorScheme='gray'>Daftar</Button>
        </Container>
      </Box>
    </>
  );
};
