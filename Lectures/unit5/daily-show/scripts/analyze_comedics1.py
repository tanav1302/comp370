import argparse
def main():
    # open the acting csv
    parser = argparse.ArgumentParser()
    parser.add_argument("acting_csv")
    args = parser.parse_args()
    acting_names = []
    with open(args.acting_csv) as f:
        f_iter = iter(f)
        header = next(f_iter) # skip the header

        for line in f_iter:
            name = line.split(",")[-1].strip()
            acting_names.append(name)

    # count the number of comedic actors
    

if __name__ == "__main__":
    main()