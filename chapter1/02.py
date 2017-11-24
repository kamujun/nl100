def alternate_character(first_sentence, second_sentence):
    first_sentence_length = len(first_sentence)
    second_sentence_length = len(second_sentence)

    first_sentence_idx = 0
    second_sentence_idx = 0
    output = ''

    while True:
        if((first_sentence_idx == first_sentence_length) or
                (second_sentence_length == second_sentence_idx)):
            break

        output = output + first_sentence[first_sentence_idx]
        output = output + second_sentence[second_sentence_idx]

        first_sentence_idx += 1
        second_sentence_idx += 1

    output = \
        output + \
        first_sentence[first_sentence_idx:first_sentence_length] + \
        second_sentence[second_sentence_idx:second_sentence_length]

    return output


if __name__ == '__main__':
    first_sentence = 'パトカー'
    second_sentence = 'タクシー'

    print(alternate_character(first_sentence, second_sentence))
