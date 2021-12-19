import { ChakraProvider, Box, Flex, VStack, Text } from '@chakra-ui/react';
import Question from './componets/Question';
import UserRank from './componets/UserRank';
import UserStatus from './componets/UserStatus';

function App() {
    return (
        <ChakraProvider>
            <VStack color="white" bg="#7cc6fe" minH="100vh" w="100vw" justify="center" align="center">
                <Flex p={10} gap={5} w="90%" justify="center" flexWrap="wrap">
                    <Question />
                    <UserStatus />
                </Flex>
                <UserRank />
            </VStack>
        </ChakraProvider>
    );
}

export default App;
