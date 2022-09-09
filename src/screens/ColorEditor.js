import React, { useReducer } from 'react';
import { Text, StyleSheet, View, Button } from 'react-native';
import ColorCounter from '../components/ColorCounter';

const COLOR_INCREMENT = 5;

function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
  }
  
function rgbToHex(r, g, b) {
    return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
  }

const reducer = (state, action) => {
    // state === {red: number, green: nember, blue: number}
    // action === {colorToChange: 'red' || 'green' || 'blue', amount: 10 || -10}

    switch (action.colorToChange) {
        case 'red': 
            return state.red + action.amount > 255 || state.red + action.amount < 0
                ? state
                :{...state, red: state.red + action.amount};
        case 'green':
            return state.green + action.amount > 255 || state.green + action.amount < 0
                ? state
                :{...state, green: state.green + action.amount};
        case 'blue':
            return state.blue + action.amount > 255 || state.blue + action.amount < 0
                ? state
                :{...state, blue: state.blue + action.amount};
        default:
            return state;
    }
};

const ColorEditor = () => {
    const [state, dispatch] = useReducer(reducer, {red: 0, green: 0, blue: 0});
    const { red, green, blue } = state;
   
    return (
    <View>
        <ColorCounter 
        onIncrease={() => dispatch({ colorToChange: 'red', amount: COLOR_INCREMENT})}
        onDecrease={() => dispatch({ colorToChange: 'red', amount: -1 * COLOR_INCREMENT})}
        color="Red" 
        />
        <ColorCounter 
        onIncrease={() => dispatch({ colorToChange: 'green', amount: COLOR_INCREMENT})}
        onDecrease={() => dispatch({ colorToChange: 'green', amount: -1 * COLOR_INCREMENT})}
        color="Green" 
        />
        <ColorCounter 
        onIncrease={() => dispatch({ colorToChange: 'blue', amount: COLOR_INCREMENT})}
        onDecrease={() => dispatch({ colorToChange: 'blue', amount: -1 * COLOR_INCREMENT})}
        color="Blue"
        />
        <View style={{height: 150, width:150, marginVertical:15, marginHorizontal:125, backgroundColor: `rgb(${red},${green},${blue})`}}/>
        <Text style={styles.color}>Color Code: {`rgb(${red},${green},${blue})`}</Text>
        <Text style={styles.color1}>HexCode: {rgbToHex(red, green, blue)}</Text>
    </View>
    );
};

const styles = StyleSheet.create({
  text: {
    fontSize: 30,
    textAlign: 'center',
    marginVertical: 45
  },
  color: {
    fontSize: 15,
    borderColor: 'black',
    borderWidth: 2,
    marginTop: 15,
    marginHorizontal: 15,
    borderRadius:5,
    textAlign: 'center'
 },
 color1: {
    fontSize: 15,
    borderColor: 'black',
    borderWidth: 2,
    margin: 15,
    borderRadius:5,
    textAlign: 'center'
 },
});

export default ColorEditor;