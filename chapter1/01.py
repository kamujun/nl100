def extract_odd_character(input_sentence):
    output = input_sentence[1::2]
    return output


if __name__ == '__main__':
    input_sentence = 'パタトクカシーー'
    print(extract_odd_character(input_sentence))
