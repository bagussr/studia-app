import { extendTheme } from '@chakra-ui/react';

export const theme = extendTheme({
  components: {
    Heading: {
      baseStyle: {
        color: 'gray.600',
      },
    },
    Link: {
      baseStyle: {
        color: 'brand.primary',
      },
    },
  },
  sizes: {
    screen: '100vh',
    half: '50%',
    '1/2': '50%',
    '1/4': '25%',
    '1/3': '33%',
    '2/3': '66%',
    '3/4': '75%',
  },
  colors: {
    brand: {
      primary: '#77BBE2',
    },
  },
});
