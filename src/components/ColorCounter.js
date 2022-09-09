import React, { useState } from 'react';
import { Text, StyleSheet, View, Button } from 'react-native';

const ColorCounter = ({color, onIncrease, onDecrease}) => {
  return (
  <View style={styles.view}>
    <Text style={styles.text}>{color}</Text>
    <Button 
    title= {`Increase ${color}`}
    onPress={() => onIncrease() }/>
    <Button 
    title= {`Decrease ${color}`}
    onPress={() => onDecrease() }/>
  </View> 
  );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
    textAlign: 'center',
    marginVertical: 15
  },
});

export default ColorCounter;