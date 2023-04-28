import Data.Char(isAlphaNum)
import Data.List(nub)

main :: IO ()
main = do
    line <- getLine
    let xs = filter isAlphaNum line
        uniques = length (nub xs)
        
    print uniques