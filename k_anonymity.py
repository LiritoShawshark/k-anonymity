def min_max(array):
    try:
        if len(array) == 1:
            return array[0], array[0]
    except Exception:
        print('Not an array')
        return 0, 0
    min = array[0]
    max = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    return min, max


if __name__ == '__main__':
    # 载入数据
    org = open('org', mode='r')
    datas = []
    while True:
        line = org.readline()
        if not line:
            break

        # 去掉\n
        line = line.strip('\n')

        # list[0]id，list[1]身份证，list[2]性别，list[3]年龄，list[4]身高，list[5]病症
        list = line.split(',')

        # 把年龄身高换回int
        list[3] = int(list[3])
        list[4] = int(list[4])

        # 去除id和身份证
        datas.append(list[2:])

    # print(datas)
    org.close()

    # 输入k值
    while True:
        k = input('输入k值：')

        try:
            if 0 < int(k) <= len(datas):
                break
        except Exception:
            pass

        print('请输入区间为[1, {}]的数'.format(len(datas)))

    # print(k)

    # 为分配最后的剩余的数据进行标杆化
    age_ranges = []
    height_ranges = []

    # 处理后数据
    oped_data = []

    # 分组处理
    k = int(k)
    groups = len(datas) // k
    remain = len(datas) % k

    # 对划分好的小组进行操作
    for i in range(groups):
        # 存储该组的性别数据，年龄数据和身高数据
        sexs = []
        ages = []
        heights = []

        # 对小组成员遍历，统计年龄数据和身高数据
        n = k if i != groups - 1 else k + remain
        for j in range(n):
            sexs.append(datas[i*k+j][0])
            ages.append(datas[i*k+j][1])
            heights.append(datas[i*k+j][2])

        # 判断该组性别是否相同
        if '男' in sexs and '女' in sexs:
            is_sex_diffirent = True
        else:
            is_sex_diffirent = False

        # 得到最小值和最大值，并填写到范围表里
        age_min, age_max = min_max(ages)
        height_min, height_max = min_max(heights)
        age_ranges.append([age_min, age_max])
        height_ranges.append([height_min, height_max])

        # 写入泛化后的数据
        for j in range(n):
            list = []
            if not is_sex_diffirent:
                list.append(datas[i * k + j][0])
            else:
                list.append('*')

            if age_ranges[i][0] != age_ranges[i][1]:
                list.append('[{}, {}]'.format(age_ranges[i][0], age_ranges[i][1]))
            else:
                list.append('*')

            if age_ranges[i][0] != age_ranges[i][1]:
                list.append('[{}, {}]'.format(height_ranges[i][0], height_ranges[i][1]))
            else:
                list.append('*')

            list.append(datas[i * k + j][3])

            oped_data.append(list)

    for op in oped_data:
        print(op)
