# Debian 7 32bit Autoscript Installer VPS
<pre><code>wget https://raw.github.com/arieonline/autoscript/master/debian7.sh
bash debian7.sh
</code></pre>
<h2>Tested on</h2>
<ul>
<li>Debian 7 32 bit</li>
<li>Debian 7 64 bit</li>
<li>OpenVZ only</li>
</ul>
<h3>What's server included</h3>
<ul>
<li>OpenSSH port 22, 143</li>
<li>OpenVPN port 1194 tcp</li>
<li>Dropbear port 80, 109, 110, 443</li>
<li>Squid port 3128, 8000, 8080 (limit to IP VPS)</li>
<li>badvpn-udpgw port 7300</li>
</ul>
<h3>What's features included</h3>
<ul>
<li>Webmin http(s)://[ip]:10000/</li>
<li>vnstat http://[ip]/vnstat/</li>
<li>MRTG http://[ip]/mrtg/</li>
<li>Timezone : Asia/Jakarta</li>
<li>Fail2Ban : [on]</li>
<li>IPv6     : [off]</li>
</ul>
<h3>What's tools included</h3>
<ul>
<li>axel</li>
<li>bmon</li>
<li>htop</li>
<li>iftop</li>
<li>mtr</li>
<li>nethogs</li>
</ul>
<h3>What's script included</h3>
<ul>
<li>screenfetch</li>
<li>ps_mem.py (<a href="https://github.com/pixelb/ps_mem/">https://github.com/pixelb/ps_mem/</a>)</li>
<li>speedtest-cli (<a href="https://github.com/sivel/speedtest-cli">https://github.com/sivel/speedtest-cli</a>)</li>
<li>bench-network.sh</li>
<li>user-login.sh</li>
<li>user-limit.sh</li>
<li>user-expire.sh</li>
</ul>
<h2>Openvpn</h2>
<pre><code>wget <a href="https://raw.github.com/arieonline/autoscript/master/dimas.debian">https://raw.github.com/arieonline/autoscript/master/dimas.debian</a>
bash dimas.debian
</code></pre>
