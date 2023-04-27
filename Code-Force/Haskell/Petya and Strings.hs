import Data.Char(toLower)

main :: IO ()
main = do
    inputs <- getContents
    let [s1, s2] = words inputs
    case compare' s1 s2 of
        EQ -> print 0
        LT -> print (-1)
        GT -> print 1

compare' :: String -> String -> Ordering
compare' s1 s2 = map toLower s1 `compare` map toLower s2