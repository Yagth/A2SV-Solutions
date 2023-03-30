
main :: IO ()
main = do
    input <- getContents
    let (first: amount) = lines input
        [people,icecream] = map read (words first)
        amount' = map readMine amount
        (restP, restI) = foldOverList (people,icecream) amount'

    putStrLn $ show restI ++ " " ++ show restP

foldOverList :: (Int, Int) -> [Int] -> (Int, Int)
foldOverList = foldl calcIceCream

readMine :: String -> Int
readMine (x:xs)
    | x == '+' = read xs'
    | otherwise = (-1) * read xs'

    where xs' = unwords . words $ xs

calcIceCream :: (Int, Int) -> Int -> (Int, Int)
calcIceCream (people, icecream) amount
    | amount > 0 = (people - 1, icecream + amount)
    | abs amount <= icecream = (people - 1, icecream + amount)
    | otherwise = (people, icecream)