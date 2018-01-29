
import time  
import sys  
import os
import argparse
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError

class downloader(object):
    def download_page(self , url):
        import urllib.request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    

    def _images_get_next_item(self , s):
        start_line = s.find('rg_di')
        if start_line == -1: 
            end_quote = 0
            link = "no_links"
            return link, end_quote
        else:
            start_line = s.find('"class="rg_meta"')
            start_content = s.find('"ou"', start_line + 1)
            end_content = s.find(',"ow"', start_content + 1)
            content_raw = str(s[start_content + 6:end_content - 1])
            return content_raw, end_content

    def _images_get_all_items(self , page):
        items = []
        mn = 0
        while mn<10:
            item, end_content = self._images_get_next_item(page)
            if item == "no_links":
                break
            else:
                items.append(item)
                time.sleep(0.1) 
                page = page[end_content:]
                mn = mn + 1
        return items

    def download(self ,keywords , color  = None):
        t0 = time.time() 
        search_keyword = [str(x) for x in keywords.split(',')]
        errorCount = 0
        i = 0
        while i < len(search_keyword):
            items = []
            iteration = "\n" + "Item no.: " + str(i + 1) + " -->" + " Item name = " + str(search_keyword[i])
            print (iteration)
            print ("Processing...")
            search_term = search_keyword[i]
            search = search_term.replace(' ', '%20')
            dir_name = search_term + ('-' + color if color else '')
            try:
                os.makedirs(dir_name)
            except OSError as e:
                if e.errno != 17:
                    raise
                pass

            j = 0
            color_param = ('&tbs=ic:specific,isc:' + color) if color else ''
            url = 'https://www.google.com/search?q=' + search + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch' + color_param + '&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
            raw_html = (self.download_page(url))
            time.sleep(0.1)
            items = items + (self._images_get_all_items(raw_html))
            #print ("Total Image Links = " + str(len(items)))

    

            t1 = time.time() 
            total_time = t1 - t0 
            #print("Total time taken: " + str(total_time) + " Seconds")
            print ("Starting Download...")
            k = 0
            success = True
            while(success):
                if k>10:
                    success = False
                try:
                    req = Request(items[k], headers={
                        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                    response = urlopen(req, None, 15)
                    image_name = str(items[k][(items[k].rfind('/'))+1:])
                    if '?' in image_name:
                        image_name = image_name[:image_name.find('?')]
                    if ".jpg" in image_name or ".png" in image_name or ".jpeg" in image_name or ".svg" in image_name:
                        output_file = open(dir_name + "/" + str(1) + ". " + image_name, 'wb')
                    else:
                        output_file = open(dir_name + "/" + str(k + 1) + ". " + image_name + ".jpg", 'wb')
                        image_name = image_name + ".jpg"
                    data = response.read()
                    output_file.write(data)
                    response.close()
                    print("completed ====> " + image_name)
                    success = False

            

                except IOError:  # If there is any IOError

                    errorCount += 1
                    print("IOError on image ")
                    k = k + 1

                except HTTPError as e:  # If there is any HTTPError

                    errorCount += 1
                    print("HTTPError")
                    k += 1
                
                except URLError as e:

                    errorCount += 1
                    print("URLError ")
                    k += 1

                i = i + 1

        print("\n")
        print("downloaded!")
        #print("Total Errors: "+ str(errorCount) + "\n")
