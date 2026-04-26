'use client'

import { useState, useEffect, useRef } from 'react'
import { Input } from '@/components/ui/button' // Wait, Input is usually from ui/input
import { Search, Building2, Check } from 'lucide-react'
import { api } from '@/lib/api'

interface Company {
  id: string
  name: string
}

interface CompanySearchProps {
  value: string // ID de l'entreprise
  onSelect: (id: string, name: string) => void
  placeholder?: string
}

export function CompanySearch({ value, onSelect, placeholder = "Rechercher une entreprise..." }: CompanySearchProps) {
  const [query, setQuery] = useState('')
  const [suggestions, setSuggestions] = useState<Company[]>([])
  const [isOpen, setIsOpen] = useState(false)
  const [loading, setLoading] = useState(false)
  const [selectedName, setSelectedName] = useState('')
  const wrapperRef = useRef<HTMLDivElement>(null)

  // Fermer la liste si on clique ailleurs
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  // Recherche auto quand l'utilisateur tape
  useEffect(() => {
    const timer = setTimeout(async () => {
      if (query.length >= 2) {
        setLoading(true)
        try {
          const response = await api.get(`company/search?q=${query}`)
          setSuggestions(response.data)
          setIsOpen(true)
        } catch (error) {
          console.error('Erreur recherche entreprise', error)
        } finally {
          setLoading(false)
        }
      } else {
        setSuggestions([])
        setIsOpen(false)
      }
    }, 300)

    return () => clearTimeout(timer)
  }, [query])

  const handleSelect = (company: Company) => {
    setSelectedName(company.name)
    setQuery(company.name)
    onSelect(company.id, company.name)
    setIsOpen(false)
  }

  const handleManualInput = () => {
    if (query.trim()) {
      onSelect(query.trim(), query.trim())
      setIsOpen(false)
    }
  }

  return (
    <div ref={wrapperRef} className="relative w-full">
      <div className="relative">
        <Building2 className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onFocus={() => query.length >= 2 && setIsOpen(true)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !isOpen) {
              handleManualInput()
            }
          }}
          placeholder={placeholder}
          className="w-full pl-10 pr-4 py-2 border border-border rounded-lg bg-background text-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all"
        />
        {loading && (
          <div className="absolute right-3 top-1/2 -translate-y-1/2">
            <div className="w-4 h-4 border-2 border-primary border-t-transparent rounded-full animate-spin" />
          </div>
        )}
      </div>

      {isOpen && suggestions.length > 0 && (
        <div className="absolute top-full mt-1 w-full bg-card border border-border rounded-lg shadow-lg z-50 overflow-hidden animate-in fade-in slide-in-from-top-2">
          {suggestions.map((company) => (
            <button
              key={company.id}
              onClick={() => handleSelect(company)}
              className="w-full flex items-center justify-between px-4 py-3 hover:bg-muted text-sm text-foreground transition-colors border-b last:border-0"
            >
              <div className="flex items-center gap-3">
                <Building2 className="w-4 h-4 text-muted-foreground" />
                <span className="font-medium">{company.name}</span>
              </div>
              {value === company.id && <Check className="w-4 h-4 text-primary" />}
            </button>
          ))}
        </div>
      )}

      {isOpen && query.length >= 2 && !loading && suggestions.length === 0 && (
        <div className="absolute top-full mt-1 w-full bg-card border border-border rounded-lg p-2 shadow-lg z-50">
          <button
            onClick={handleManualInput}
            className="w-full flex items-center gap-3 px-4 py-3 hover:bg-muted text-sm text-foreground transition-colors rounded-md"
          >
            <Building2 className="w-4 h-4 text-primary" />
            <div className="text-left">
              <div className="font-medium">Utiliser "{query}"</div>
              <div className="text-xs text-muted-foreground">Cette entreprise sera ajoutée à la base de données.</div>
            </div>
          </button>
        </div>
      )}
    </div>
  )
}
