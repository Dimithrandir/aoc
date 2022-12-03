def solve_part_one(data):
    gamma_rate = ''
    epsilon_rate = ''
    one_nums = 12 * [0]

    for num in data:
        for i in range(len(num)):
            if num[i] == '1':
                one_nums[i] += 1

    for i in range(len(one_nums)):
        if one_nums[i] > len(data) / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

def solve_part_two(data):
    
    def find_most_common_bits(numbers):
        # total number of '1' on each position in the set
        one_nums = 12 * [0]

        for num in numbers:
            for i in range(len(num)):
                if num[i] == '1':
                    one_nums[i] += 1

        for i in range(len(one_nums)):
            one_nums[i] = 1 if one_nums[i] >= len(numbers) / 2 else 0

        return one_nums

    ogr = ''
    co2sr = ''
    ogr_nums = data
    co2sr_nums = data

    for i in range(len(data)):
        bits1 = find_most_common_bits(ogr_nums)
        bits2 = find_most_common_bits(co2sr_nums)
        new_ogr_nums = []
        new_co2sr_nums = []

        if len(ogr_nums) > 1:
            for num in ogr_nums:
                if num[i] == str(bits1[i]):
                    new_ogr_nums.append(num)
            ogr_nums = new_ogr_nums

        if len(co2sr_nums) > 1:
            for num in co2sr_nums:
                if num[i] != str(bits2[i]):
                    new_co2sr_nums.append(num)
            co2sr_nums = new_co2sr_nums

    for i in range(len(ogr_nums)):
        ogr += str(ogr_nums[i])
        co2sr += str(co2sr_nums[i])

    ogr = int(ogr, 2)
    co2sr = int(co2sr, 2)

    print(ogr * co2sr)

if __name__ == "__main__":

    with open("input") as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
