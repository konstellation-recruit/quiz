import { Image, VStack } from '@chakra-ui/react';
import { useSelector } from 'react-redux';

export default function MemeImage() {
    const url = useSelector((state) => state.image);

    return (
        <VStack p={5} boxShadow="dark-lg" borderRadius={20} justify="center" align="center" w="400px" h="350px" bg="#252d4a">
            <Image src={url} />
        </VStack>
    );
}
