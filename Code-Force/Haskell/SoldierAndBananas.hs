main :: IO()
main = do
    inputs <- getLine
    let input = map read $ words inputs
    print $ cost input 

cost :: [Int] -> Int
cost [k,n,w] | borrow < 0 = 0 | otherwise = borrow
    where borrow = flip (-) n $  sum . take w . map (*k) $ [1..]