book_pages=input("please enter count of pages:")
book_pages=int(book_pages)
book_cap=book_pages*240
mem_cap=input("please enter memory capacity(GB)")
mem_cap=int(mem_cap)
mem_capB=mem_cap*(1024**3)
book_count=mem_capB/book_cap
print(book_count)