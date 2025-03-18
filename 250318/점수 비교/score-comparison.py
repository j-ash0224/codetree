A_math_score, A_english_score = map(int, input().split());
B_math_score, B_english_score = map(int, input().split());

if A_math_score>B_math_score and A_english_score>B_english_score:
    print(1);
else:
    print(0);

