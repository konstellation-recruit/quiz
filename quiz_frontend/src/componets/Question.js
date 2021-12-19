import { Box, Text, VStack, Button, HStack } from '@chakra-ui/react';
import Timer from './TImer';

export default function Question() {
    return (
        <VStack p={5} boxShadow="dark-lg" borderRadius={20} justify="space-between" w="400px" h="350px" bg="#252d4a">
            <HStack>
                <Text>1/10</Text>
            </HStack>
            <Text>Lorem ipsum dolor sit amet, consectetur adip</Text>
            <Timer />
        </VStack>
    );
}
