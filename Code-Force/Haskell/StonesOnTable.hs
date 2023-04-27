import Data.List(group)

main :: IO ()
main = do
    input <- getContents
    let (_:stones) = words input
    print $ colorToRemove (concat stones)

colorToRemove :: String -> Int
colorToRemove xs = sum (manyGroups xs) - length (manyGroups xs)
    where manyGroups = filter (>1) . map length . group