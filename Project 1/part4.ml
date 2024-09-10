(* Memoized DP *)
let memo = Hashtbl.create 100000;;

let rec generate_pascals_triangle n k =
  if n = 0 || k = 0 || k = n then 1 (*base*)
  else
    try Hashtbl.find memo (n, k)
    with Not_found ->
      let result = generate_pascals_triangle (n - 1) (k - 1) + generate_pascals_triangle (n - 1) k in
      Hashtbl.add memo (n, k) result;
      result
;;

(* print pascal's triangle *)
let print_triangle n =
  for i = 0 to n - 1 do
    for j = 0 to i do
      Printf.printf "%d " (generate_pascals_triangle i j)
    done;
    print_newline ()
  done
;;

let () =
  let n = int_of_string Sys.argv.(1) in
  print_triangle n
