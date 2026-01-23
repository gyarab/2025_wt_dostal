import httpx

res = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt')

print("Server odpovedel", res.status_code)

lines = res.text.split('\n')
print("Kurzy pro den:", lines[0].split(' ')[0])