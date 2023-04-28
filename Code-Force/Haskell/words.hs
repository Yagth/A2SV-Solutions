import Data.Char 

main :: IO ()
main = interact word

word :: String -> String
word s | uppers > lowers = map toUpper s | otherwise = map toLower s
    where lowers = length . filter isLower $ s
          uppers = length . filter isUpper $ s