import { Text, VStack } from '@chakra-ui/react';

export default function UserRank() {
    return (
        <VStack borderRadius={20} boxShadow="dark-lg" p={10} maxH="340px" w="400px" bg="#252d4a">
            <Text>User Score</Text>
            <VStack flexWrap="wrap" w="full" maxH="250px">
                <Text>1. Dongchang</Text>
                <Text>2. Dongchang</Text>
                <Text>3. Dongchang</Text>
                <Text>4. Dongchang</Text>
                <Text>5. Dongchang</Text>
                <Text>6. Dongchang</Text>
                <Text>7. Dongchang</Text>
                <Text>8. Dongchang</Text>
                <Text>9. Dongchang</Text>
                <Text>10. Dongchang</Text>
                <Text>11. Dongchang</Text>
                <Text>12. Dongchang</Text>
            </VStack>
        </VStack>
    );
}
