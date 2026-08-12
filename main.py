"""나만의 퀴즈 게임 — 한국사 편"""


def ask_number(prompt, low, high):
    """low~high 사이의 정수를 받을 때까지 계속 물어본다.

    공백 제거, 빈 입력, 숫자 아님, 범위 밖을 모두 여기서 처리한다.
    숫자를 입력받는 곳은 전부 이 함수를 사용한다.
    """
    while True:
        text = input(prompt).strip()

        if text == '':
            print(f'⚠  입력이 비어 있습니다. {low}-{high} 사이의 숫자를 입력하세요.')
            continue

        try:
            number = int(text)
        except ValueError:
            print(f'⚠  숫자가 아닙니다. {low}-{high} 사이의 숫자를 입력하세요.')
            continue

        if low <= number <= high:
            return number

        print(f'⚠  {low}-{high} 범위를 벗어났습니다. 다시 입력하세요.')


class Quiz:
    """퀴즈 한 문제를 표현한다. (문제 / 선택지 4개 / 정답 번호)"""

    def __init__(self, question, choices, answer):
        self.question = question    # 문제 문장 (문자열)
        self.choices = choices      # 선택지 4개 (리스트)
        self.answer = answer        # 정답 번호 1~4 (정수)

    def show(self, number):
        """문제 번호와 함께 문제와 선택지를 출력한다."""
        print(f'\n[문제 {number}] {self.question}')
        for index, choice in enumerate(self.choices, start=1):
            print(f'  {index}. {choice}')

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False."""
        return user_answer == self.answer


def default_quizzes():
    """저장 파일이 없거나 손상됐을 때 사용할 기본 한국사 퀴즈 6문제."""
    return [
        Quiz('조선의 4대 왕으로 훈민정음을 창제한 인물은?',
             ['태조', '정조', '세종대왕', '영조'], 3),
        Quiz('임진왜란이 일어난 연도는?',
             ['1492년', '1592년', '1636년', '1910년'], 2),
        Quiz('고구려를 건국한 인물은?',
             ['주몽', '온조', '박혁거세', '왕건'], 1),
        Quiz('우리나라 최초의 국가인 고조선을 세운 인물은?',
             ['단군왕검', '이성계', '궁예', '대조영'], 1),
        Quiz('현존하는 세계에서 가장 오래된 금속 활자본은?',
             ['팔만대장경', '직지심체요절', '조선왕조실록', '삼국사기'], 2),
        Quiz('후삼국을 통일하고 고려를 건국한 인물은?',
             ['견훤', '궁예', '왕건', '대조영'], 3),
    ]


def show_menu():
    """메뉴 화면을 출력한다."""
    print()
    print('=' * 40)
    print('        🎯  나만의 퀴즈 게임  🎯')
    print('=' * 40)
    print('1. 퀴즈 풀기')
    print('2. 퀴즈 추가')
    print('3. 퀴즈 목록')
    print('4. 점수 확인')
    print('5. 종료')
    print('=' * 40)


def main():
    """프로그램의 시작점. 메뉴를 반복해서 보여준다."""
    quizzes = default_quizzes()
    print(f'\n📂 기본 퀴즈 {len(quizzes)}개를 불러왔습니다.')

    while True:
        show_menu()
        choice = ask_number('선택: ', 1, 5)

        if choice == 1:
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 풀기)')
        elif choice == 2:
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 추가)')
        elif choice == 3:
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 목록)')
        elif choice == 4:
            print('\n(아직 만들지 않은 기능입니다: 점수 확인)')
        elif choice == 5:
            print('\n게임을 종료합니다. 안녕히 가세요!')
            break


if __name__ == '__main__':
    main()
