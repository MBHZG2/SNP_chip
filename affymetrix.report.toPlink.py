import sys

def process_affy_file(affy):
    with open(affy, 'r') as file1:
        for line in file1:
            items = line.split()
            chromosome = items[3]
            snp_id = items[1]
            genotype = "0"
            position = items[5]
            geno_value = items[4]

            if geno_value == "NOCALL":
                geno_value = " ".join("00")

            geno_value = " ".join(geno_value)
            data = [chromosome, snp_id, genotype, position, geno_value]

            if chromosome != "RS":
                print("\t".join(data))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <affy_file>")
        sys.exit(1)

    affy_file = sys.argv[1]
    process_affy_file(affy_file)
