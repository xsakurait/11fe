a='ABCBADABC'

print(a.count('ABC'))#aの中にあるABCを数えるので、２が表示

print(a.startswith('ABC')#「何で始まるか」なのでTrue

print(a.endswith('DE')#[何で終わるか」よりFalse

b=' ABC '

print(b.strip())#両端の()の文字列消すので「ABC」

print(b.l(left)strip())#左側の()の文字列消すので「ABC 」

print(b.r(right)strip())#右側の文字列消すので「 ABC」

b='ABCDEABC'

print(b.strip('CBA')#両端のABC１つ消してDE

print(b.lstrip('CBA')#左端のABC１つ消してDEABC

print(b.rstrip('CBA')#右端のABC１つ消してABCDE

a='hello, my name is taro'

print(a[6:])# my name is taro

name='Jiro'

print(f'hello{name}')#hello Jiro

printf'{name=}')#name=Jiro

print(name.isupper())#すべて大文字=True この場合False

print(name.islower())#すべて小文字＝Ｔｒｕｅ　この場合False

a='ABCABC'

print(a.find('ABC'))#左端からABC探す　0

print(a.rfind('ABC'))#右端からABC探す 3

print(a.index('ABC'))#左端からABC探す　0

print(a.rindex('ABC'))#右端からABC探す　3

index,findで違うのは値が見つからないとき、find=-1 index=エラーを表示するので

indexだと後の処理が実行されずに終わる