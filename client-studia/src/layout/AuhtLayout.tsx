import * as react from 'react';
import { Outlet } from 'react-router-dom';
import { Box, Image } from '@chakra-ui/react';

import base from '../assets/images/auth-base.png';

export const AuthLayout: react.FC = () => {
  return (
    <>
      <Box display='flex' w='full' minH='screen' as='main'>
        <Box as='section' display='flex' w='full'>
          <Outlet />
        </Box>
        <Box display={{ md: 'flex', base: 'none' }} p='2' as='section'>
          <Image src={base} alt='auth bannner' w='full' />
        </Box>
      </Box>
    </>
  );
};
