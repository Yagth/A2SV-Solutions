main :: IO()
main = do
    inputs <- getContents
    let (_:statements) = inputs
        result = foldl (\acc x -> exec acc . parser $ x) 0 (lines statements)
    print result

data Operation = AddOne | SubOne | Undefined deriving Show

parser :: String -> Operation
parser "++X" = AddOne
parser "--X" = SubOne
parser "X++" = AddOne
parser "X--" = SubOne
parser xs = Undefined

exec :: Integer -> Operation -> Integer
exec x AddOne = x + 1
exec x SubOne = x - 1
exec x Undefined= x

