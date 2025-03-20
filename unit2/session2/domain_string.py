
def subdomain(domain):
    string = domain.split(".")
    array = []
    answer = ""
    for i in range(len(string)-1, -1, -1):
        if i == len(string) -1:
            answer = string[i]
            array.append(answer)
            continue
        answer = string[i] + "." + answer
        array.append(answer)
    return array

def subdomain_visits(cpdomains):
    new_dictionary = {}
    for item in cpdomains:
        count, domain  = item.split(" ")
        subdomains = subdomain(domain)
        for sub in subdomains:
            if sub not in new_dictionary:
                new_dictionary[sub] = 0
            new_dictionary[sub] += int(count)
    results = []
    for key, val in new_dictionary.items():
        print(key,val)
        ans = str(val) + " " + str(key)
        results.append(ans)
    return results

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))