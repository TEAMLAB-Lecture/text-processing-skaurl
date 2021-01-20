#######################
# Test Processing I   #
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""


def normalize(input_string):
    """
     인풋으로 받는 스트링에서 정규화된 스트링을 반환함
     아래의 요건들을 충족시켜야함
    * 모든 단어들은 소문자로 되어야함
    * 띄어쓰기는 한칸으로 되어야함
    * 앞뒤 필요없는 띄어쓰기는 제거해야함

         Parameters:
             input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
             ex - "This is an example.", "   EXTRA   SPACE   "

         Returns:
             normalized_string (string): 위 요건을 충족시킨 정규회된 string
             ex - 'this is an example.'

         Examples:
             # >>> import text_processing as tp
             # >>> input_string1 = "This is an example."
             # >>> tp.normalize(input_string1)
             'this is an example.'
             # >>> input_string2 = "   EXTRA   SPACE   "
             # >>> tp.normalize(input_string2)
             'extra space'
    """
    normalized_string = " ".join([i.lower() for i in input_string.split()])
    '''
    1. split()으로 문자열의 띄어쓰기를 제거하며 리스트로 변환
        * 앞뒤 필요없는 띄어쓰기는 제거해야함
    2. lower()으로 리스트의 원소를 소문자로 변환
        * 모든 단어들은 소문자로 되어야함
    3. join()으로 리스트의 원소 사이사이에 띄어쓰기를 추가하며 문자열로 변환
        * 띄어쓰기는 한칸으로 되어야함
    '''
    return normalized_string


def no_vowels(input_string):
    """
    인풋으로 받는 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호로 이루어진 string
            ex - "This is an example."

        Returns:
            no_vowel_string (string): 모든 모음 (a, e, i, o, u)를 제거시킨 스트링
            ex - "Ths s n xmpl."

        Examples:
            # >>> import text_processing as tp
            # >>> input_string1 = "This is an example."
            # >>> tp.normalize(input_string1)
            "Ths s n xmpl."
            # >>> input_string2 = "We love Python!"
            # >>> tp.normalize(input_string2)
            ''W lv Pythn!'
    """
    no_vowel_string = ""
    for i in input_string:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            # input_string의 문자열 i가 a,e,i,o,u,A,E,I,O,U면 no_vowel_string에 추가하지 않는다.
            continue
        else:
            # input_string의 문자열 i가 a,e,i,o,u,A,E,I,O,U가 아니면 no_vowel_string에 추가한다.
            no_vowel_string += i
    return no_vowel_string
