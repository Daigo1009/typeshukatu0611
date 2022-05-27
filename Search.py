def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 真ん中を見つける
    while len(sorted_array) > 2 :
        point = -(-len(sorted_array)//2)
    
    # 真ん中の値が目的の値よりも小さい場合
        if sorted_array[point] < target_number :
            del sorted_array[1:point]
            print(sorted_array)
        
    # 真ん中の値が目的の値より大きい場合   
        elif sorted_array[point] > target_number :
            del sorted_array[point:-1]
            print(sorted_array)
            
    # 真ん中の値と目的の値が等しい場合        
        elif sorted_array[point] == target_number :
            print(sorted_array[point])
            del sorted_array[0:point]
            del sorted_array[point+1:]

    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
