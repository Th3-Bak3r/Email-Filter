from os.path import splitext

def classify_emails(input_file):
     banner = """
    
    ██████╗  █████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
    ██████╔╝███████║█████╔╝ █████╗  ██████╔╝
    ██╔══██╗██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██████╔╝██║  ██║██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ Email Filter By https://t.me/BAK34_TMW / Discord: https://discord.com/users/825505380452925470
    """

    domains = {}

    with open(input_file, 'r') as file:
        for line in file:
            email = line.strip()
            if '@' in email:
                _, domain = email.split('@', 1)
                domain = domain.lower()

                if domain not in domains:
                    domains[domain] = []

                domains[domain].append(email)

    return domains

def save_domains(domains):
    for domain, emails in domains.items():
        output_file = f"{domain}.txt"
        with open(output_file, 'w') as file:
            for email in emails:
                file.write(f"{email}\n")

if __name__ == "__main__":
    print(banner)
    input_file = input("Enter the path of the input file: ")
    domains = classify_emails(input_file)
    save_domains(domains)
    print("Emails classified successfully!")