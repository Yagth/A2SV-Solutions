import Data.List(sort, group)

main :: IO()
main = do
    input <- getLine
    let inputs = (group . sort) $ map read (words input)
        largeInputs = largeGroup inputs
        properLargeInputs = map (properInputs largeInputs) takeLength
        minSum = properLargeInputs + (sum . concat) (smallGroup inputs)
    print minSum


properInputs :: [[Integer]] -> Integer -> [Integer]
properInputs largeInputs tl = map (sum . take (fromIntegral tl)) largeInputs

minimum' :: [Integer] -> Integer
minimum' [] = 0
minimum' xs = minimum xs

takeLength :: [Integer] -> [Integer]
takeLength group
    | length group <= 3 = [fromIntegral $ length group]
    | otherwise = [2,3]

largeGroup :: [[Integer]] -> [[Integer]]
largeGroup [] = []
largeGroup group =  filter (\x -> length x >= 2) group

smallGroup :: [[Integer]] -> [[Integer]]
smallGroup [] = []
smallGroup group = filter (\x -> length x == 1) group