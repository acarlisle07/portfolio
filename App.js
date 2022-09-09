import * as React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import ColorEditor from './src/screens/ColorEditor';

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="HexCode Generator" component={ColorEditor} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;

