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
