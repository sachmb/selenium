{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'selenium'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-887f22944581>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommon\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeys\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mKeys\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mselenium\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwebdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mchrome\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0moptions\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mOptions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'selenium'"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Options' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-6492de6b6a30>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#adding options on chrome\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mchromeOptions\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mOptions\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mchromeOptions\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd_argument\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"--kiosk\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Options' is not defined"
     ]
    }
   ],
   "source": [
    "#adding options on chrome\n",
    "chromeOptions = Options()\n",
    "chromeOptions.add_argument(\"--kiosk\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'webdriver' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-1cc02ea8e22a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdriver\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0moptions\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchromeOptions\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"https://www.pluralsight.com/\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mele\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_eleement_by_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"q\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'webdriver' is not defined"
     ]
    }
   ],
   "source": [
    "driver = webdriver.Chrome(options=chromeOptions)\n",
    "driver.get(\"https://www.pluralsight.com/\")\n",
    "\n",
    "ele = driver.find_eleement_by_name(\"q\")\n",
    "time.sleep(1)\n",
    "ele.clear()\n",
    "ele.send_keys(\"Pratheerth Padman\")\n",
    "ele.send_keys(Keys.RETURN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'driver' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-edc6c27c0986>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'driver' is not defined"
     ]
    }
   ],
   "source": [
    "driver.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
