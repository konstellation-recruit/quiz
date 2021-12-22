import { useEffect, useState } from 'react';
import { ChakraProvider, Box, Flex, VStack, Text, Input, Button } from '@chakra-ui/react';
import Question from './componets/Question';
import UserRank from './componets/UserRank';
import UserStatus from './componets/UserStatus';
import { useDispatch, useSelector } from 'react-redux';
import { updateUserId } from './actions';

function App() {
    const [signed, setSigned] = useState(false);
    const [name, setName] = useState();
    const [email, setEmail] = useState();

    const dispatch = useDispatch();

    useEffect(() => {
        const userId = window.localStorage.getItem('user_id');
        if (userId) {
            setSigned(true);
            dispatch(updateUserId(userId));
        }
    }, []);

    const handleNameChange = (e) => {
        setName(e.target.value);
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handleSubmit = async () => {
        console.log(name, email);

        window.localStorage.setItem('user_id', email);
        setSigned(true);
    };

    return (
        <ChakraProvider>
            <VStack color="white" bg="#7cc6fe" minH="100vh" w="100vw" justify="center" align="center">
                {signed ? (
                    <>
                        <Flex p={10} gap={5} w="90%" justify="center" flexWrap="wrap">
                            <Question />
                            <UserStatus />
                        </Flex>
                        <UserRank />
                    </>
                ) : (
                    <VStack p={5} w="300px" h="300px" bg="#252d4a" borderRadius={20} boxShadow="dark-lg" justify="center" align="center" spacing={6}>
                        <Text fontSize="2xl">Login</Text>
                        <VStack>
                            <Input type="text" placeholder="name" onChange={handleNameChange} />
                            <Input type="email" placeholder="email" onChange={handleEmailChange} />
                        </VStack>
                        <Button color="black" onClick={handleSubmit}>
                            Submit
                        </Button>
                    </VStack>
                )}
            </VStack>
        </ChakraProvider>
    );
}

export default App;
