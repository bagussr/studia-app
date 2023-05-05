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
    Button: {
      variants: {
        google: {
          bg: 'white',
          border: '2px solid',
          borderColor: 'gray.200',
          _hover: {
            bg: 'gray.200',
          },
          _active: {
            bg: 'gray.300',
          },
        },
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
