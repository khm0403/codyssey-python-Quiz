"""나만의 퀴즈 게임 — 한국사 편"""


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
        choice = input('선택: ').strip()

        if choice == '1':
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 풀기)')
        elif choice == '2':
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 추가)')
        elif choice == '3':
            print('\n(아직 만들지 않은 기능입니다: 퀴즈 목록)')
        elif choice == '4':
            print('\n(아직 만들지 않은 기능입니다: 점수 확인)')
        elif choice == '5':
            print('\n게임을 종료합니다. 안녕히 가세요!')
            break
        else:
            print('\n⚠  잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.')


if __name__ == '__main__':
    main()
