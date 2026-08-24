/* Bilförsäkringspriser.se — v2.js
   Ingen beroenden. Allt är progressive enhancement: sidan fungerar utan JS. */
(function () {
  'use strict';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ── Affiliatemål ────────────────────────────────────────────────
     ÄNDRA HÄR när partneravtalet är på plats. utm_content sätts per
     sida så att det går att se vilken sida som konverterar — förutsatt
     att partnern vidarebefordrar parametern. Fråga dem om fältnamnet;
     vissa nätverk använder "subid" i stället.                        */
  var AFF_BASE = 'https://www.example-partner.se/jamfor';
  var SLUG = (location.pathname.replace(/^\/|\/$/g, '') || 'start').replace(/\//g, '-');
  var AFF = AFF_BASE
    + (AFF_BASE.indexOf('?') > -1 ? '&' : '?')
    + 'utm_source=bilforsakringspriser&utm_medium=web&utm_campaign=organisk'
    + '&utm_content=' + encodeURIComponent(SLUG);

  /* ── Registreringsnummer: formatering ABC 123 / ABC 12A ────────── */
  function fmt(raw) {
    var v = raw.toUpperCase().replace(/[^A-ZÅÄÖ0-9]/g, '').slice(0, 6);
    return v.length > 3 ? v.slice(0, 3) + ' ' + v.slice(3) : v;
  }
  function plateValue(inp) {
    return inp ? inp.value.replace(/\s/g, '').toUpperCase() : '';
  }
  var SWE_PLATE = /^[A-ZÅÄÖ]{3}[0-9]{2}[0-9A-ZÅÄÖ]$/;

  $$('[data-plate]').forEach(function (inp) {
    inp.addEventListener('input', function () {
      this.value = fmt(this.value);
      var ok = SWE_PLATE.test(plateValue(this));
      this.setAttribute('aria-invalid', this.value && !ok ? 'true' : 'false');
    });
  });

  /* ── Vidare till partnern ──────────────────────────────────────── */
  function go(plate) {
    var url;
    try { url = new URL(AFF); }
    catch (e) { window.open(AFF, '_blank', 'noopener,noreferrer'); return; }
    if (plate) url.searchParams.set('regnr', plate);
    window.open(url.toString(), '_blank', 'noopener,noreferrer');
  }

  $$('[data-go]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('data-go');
      var inp = id ? document.getElementById(id) : null;
      var plate = plateValue(inp);
      if (plate && !SWE_PLATE.test(plate)) {
        inp.setAttribute('aria-invalid', 'true');
        inp.focus();
        return;
      }
      go(plate);
    });
  });

  /* Enter i fältet skickar vidare */
  $$('[data-plate]').forEach(function (inp) {
    inp.addEventListener('keydown', function (e) {
      if (e.key !== 'Enter') return;
      e.preventDefault();
      var btn = document.querySelector('[data-go="' + inp.id + '"]');
      if (btn) btn.click();
    });
  });

  /* ── Meny på mobil ─────────────────────────────────────────────── */
  var burger = $('.burger'), nav = $('.nav');
  if (burger && nav) {
    burger.setAttribute('aria-expanded', 'false');
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
        burger.focus();
      }
    });
  }

  /* ── Undermenyer ───────────────────────────────────────────────
     Länkarna finns i HTML även utan JS — här läggs bara öppning,
     stängning och tangentbordsstöd på. */
  var navItems = $$('.nav-item');
  function stangAlla(utom) {
    navItems.forEach(function (it) {
      if (it === utom) return;
      it.classList.remove('open');
      var b = $('.nav-btn', it);
      if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  navItems.forEach(function (item) {
    var btn = $('.nav-btn', item);
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = item.classList.contains('open');
      stangAlla(item);
      item.classList.toggle('open', !open);
      btn.setAttribute('aria-expanded', !open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('.nav-item')) stangAlla(null);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var oppen = navItems.filter(function (i) { return i.classList.contains('open'); })[0];
    if (oppen) {
      stangAlla(null);
      var b = $('.nav-btn', oppen);
      if (b) b.focus();
    }
  });

  /* ── FAQ ───────────────────────────────────────────────────────── */
  $$('.q-btn').forEach(function (btn) {
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', function () {
      var q = btn.closest('.q');
      var open = q.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ── Klibbig CTA — visas när hjältekortet lämnat vyn ───────────── */
  var sticky = $('.sticky');
  var anchor = $('#heroPlate') || $('#pagePlate') || $('.plate');
  if (sticky && anchor && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (e) {
      sticky.classList.toggle('show', !e[0].isIntersecting);
    }, { threshold: 0 }).observe(anchor);
  }
})();
