import random


def get_integer(prompt):
    """获取用户输入的整数，非整数时提示重新输入"""
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("⚠ 请输入一个有效的整数！")


def main():
    print("=" * 40)
    print("       💩 猫屎游戏 💩")
    print("=" * 40)
    print()

    # 设置范围
    min_val = get_integer("请输入最小值: ")
    while True:
        max_val = get_integer("请输入最大值: ")
        if max_val > min_val:
            break
        print(f"⚠ 最大值必须大于最小值 {min_val}！")

    # 选择目标数字
    print()
    print(f"范围: {min_val} ~ {max_val}")
    choice = input("手动设置目标数字还是随机生成？(输入数字 / 按回车随机生成): ").strip()

    if choice == "":
        target = random.randint(min_val, max_val)
    else:
        while True:
            try:
                target = int(choice)
                if min_val <= target <= max_val:
                    break
                print(f"⚠ 目标数字必须在 {min_val} ~ {max_val} 范围内！")
            except ValueError:
                print("⚠ 请输入一个有效的整数！")
            choice = input("请重新输入目标数字: ").strip()

    print()
    print("=" * 40)
    print(f"🎯 目标数字: {target}")
    print("🎮 游戏开始！")
    print("=" * 40)

    # 游戏循环
    low = min_val
    high = max_val
    display_low = min_val
    display_high = max_val
    rounds = 0

    while True:
        print(f"\n当前范围: {display_low} ~ {display_high}  |  🎯 目标: {target}")
        guess = input("请输入你猜的数字: ").strip()

        # 检查是否为整数
        try:
            guess = int(guess)
        except ValueError:
            print("⚠ 无效输入！请输入一个整数。")
            continue

        # 检查是否在有效范围内（实际范围）
        if guess < low or guess > high:
            print(f"⚠ 无效输入！数字必须在 {display_low} ~ {display_high} 范围内。")
            continue

        rounds += 1

        if guess == target:
            print()
            print("=" * 40)
            print(f"💩 恭喜！数字就是 {target}！")
            print(f"   你就是铲猫屎的人！（第 {rounds} 轮）")
            print("=" * 40)
            break
        elif guess < target:
            low = guess + 1
            display_low = guess
            print(f"📈 太小了！范围缩小为 {display_low} ~ {display_high}")
        else:
            high = guess - 1
            display_high = guess
            print(f"📉 太大了！范围缩小为 {display_low} ~ {display_high}")

    # 再来一局
    print()
    again = input("再来一局？(y/n): ").strip().lower()
    if again == "y":
        print()
        main()
    else:
        print("👋 下次再来铲猫屎吧！")


if __name__ == "__main__":
    main()
