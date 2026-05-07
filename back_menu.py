def back_to_menu():

    print("\n" + "="*40)
    choice = input("0을 입력하면 다시 '타입 선택'으로 돌아갑니다 (종료는 q): ")
    
    if choice == "0":
        return True  # 처음화면
    elif choice.lower() == "q":
        return False # 종료
    
    return None