def main():
    sum_of_sqs = sum(i**2 for i in range(1, 101))
    sq_of_sum  = sum(range(1, 101))**2
    print(sq_of_sum - sum_of_sqs)

if __name__ == "__main__":
    main()
